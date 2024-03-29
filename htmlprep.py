from math import ceil
import subprocess
import os

class htmlgen:

    def __init__(self, filename):
        self.filename = f"{filename}"

    def header_adder(self, text):
        return """<html><body style="font-size: 1.5rem; font-family: Arial; background-color: #e7d6c0;">""" + text + "</body></html>"

    def word_processor(self, word:str):

        len_to_bold = ceil(word.__len__()/2)
        return "<B>" + word[0: len_to_bold] + "</B>" + word[len_to_bold:]

    def text_processor(self, text:str):

        """Run This"""
        
        self.line_split = text.split(". ")
        self.output = []
        n = 0
        for i in self.line_split:

            text_data = i.split(" ")
            self.output.append(f"""<p style="border-style: ridge; border-color:#14213d;padding: 15px;">{n + 1}: """)
            for j in text_data:
                temp = self.word_processor(j)
                self.output.append(temp)

            self.output.append(".</p>")
            n += 1
        self.output_text = " ".join(self.output)
        #print(self.output_text)
        #print(" ".join(output))
        with open(f"{self.filename}.html", "w") as f:
            f.write(self.header_adder(self.output_text))
        self.run()
    

    def run(self):

        url = f"{self.filename}.html"
        try: # should work on Windows
            os.startfile(url)
        except AttributeError:
            try: # should work on MacOS and most linux versions
                subprocess.call(['open', url])
            except:
                print('Could not open URL')