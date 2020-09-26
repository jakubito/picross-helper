# Picross Helper

This is a simple calculator for [nonograms](https://en.wikipedia.org/wiki/Nonogram) (aka picross / griddlers).
It calculates a sequence of squares to be filled within a line, based on hint numbers ([explained here](https://en.wikipedia.org/wiki/Nonogram#Mathematical_Approach)).
I wrote this script to save me time when solving lines in big puzzles (I'm talking 100 - 150 squares long).

https://picross-helper.jakubito.repl.run

## Installation

Simply [download](https://github.com/jakubito/picross-helper/archive/master.zip) the script to your computer and run it with python (v3 required):

```
python main.py
```

## Usage

After entering a line length, simply enter a hint sequence.
If there are squares to be filled, they will be printed as a sequence together with blank squares.

In an example below, the output is 2 empty squares, followed by 4 filled squares and so on:

```
Enter line length: 15

> 6 6
2 ⟶ [4] ⟶ 3 ⟶ [4]
```

Type `exit` to exit the program.

## Bug reporting

If you find a bug, please send me an e-mail to dobes.jakub@gmail.com or open an issue here on github.

## License

ISC
