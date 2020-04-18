# roll_stats
Playing with different ways to roll DnD 5e stats. Taken from this thread on [Geek Native](https://www.geeknative.com/61483/12-different-ways-roll-dnd-character/). 

## Usage
The script is already configured to run the base caes from the thread. Just run it:
```
% python roll_it.py
3d6: 				[12, 11, 10, 10, 9, 5]
4d6: 				[16, 16, 13, 13, 12, 8]
5d6: 				[17, 16, 16, 15, 15, 14]
2d6+6				[15, 14, 13, 12, 11, 8]
4d6 (6 of 8):			[17, 15, 14, 14, 14, 13]
4d6, reroll below 8:		[16, 11, 11, 10, 9, 9]
4d6, never below 8:		[17, 15, 14, 14, 13, 10]
4d6, reroll if none > 15:	[16, 14, 13, 11, 10, 9]
4d6, reroll if total < 70:	[16, 13, 13, 12, 11, 7]
4d6, reroll 1s:			[18, 16, 14, 13, 11, 10]
4d6, only one can be > 16:	[17, 13, 12, 11, 9, 8]
```

If you want to change the rule, tweak the variable defaults in the various higher-level functions.
