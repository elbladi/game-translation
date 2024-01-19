# Card's Game Tanslation

Simple App to translate a game cards text into a spanish card. From card images 👽️

## 📝 What you need?

- A root folder named `images`
- the images from where you will extract the text. `jpeg`, `png` `jpg` only will be read. Other files will get ignored. 🧐
- Python 3.11.6

## How to use

1. Get your images in the `images` folder
2. execute `generate_data.py`. It'll generate `data.json` file.
3. Do a human review to translations. And do changes accordingly.
   - Sometimes the translation is off due to english text used to translate is different than what you expected. The reason could be the image wasn't clear enough to get the text, or the algorithm is just dumb. If you face this issue, (_like i did_), try to replace your image for one more sharp.
4. Execute `create_cards.py`. It'll generate `cards.docx` file.
