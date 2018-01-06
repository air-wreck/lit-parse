# lit-parse
a program that plots Vonnegut's shapes of stories with questionable accuracy

Essentially, this program takes a provided input text and does some simple natural language processing to determine the sentiment polarity of a chunk of text. The polarity versus time (as measured by the progression of sentences) is then plotted. A polarity of -1 indicates 'very bad', and a polarity of +1 indicates 'very good'. 

Of course, a rather large flaw in this process is that it can't handling nonlinear/non-chronological texts. Also, the accuracy is sort of questionable.

### usage
You can use the program simply by running `python main.py`. By default, it will read the input text from the provided `input.txt` file and will analyze each sentence separately. You can modify this behavior by specifying the input file and the step. When you specify a step of `n`, the program averages the polarity across every `n` sentences (probably not the best way of doing it, but oh well). For example, to analyze the provided `cinderella.txt` file with step 3, you could run 
```bash
python main.py cinderella.txt 3
``` 

### dependencies
This program uses [TextBlob](http://textblob.readthedocs.io/en/dev/) for natural language processing. You can install TextBlob with
```bash
pip install -U textblob
```
This program also uses [matplotlib](https://matplotlib.org/) for grpahing. You can install matplotlib with
```bash
python -mpip install -U matplotlib
```

