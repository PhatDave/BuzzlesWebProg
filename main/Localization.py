class Localization:
	def __init__(self):
		self.content = {
			'skyscrapers': {
				'en': {
					'puzzleName': 'skyscrapers',
					'puzzleTitle': 'Skyscrapers',
					'puzzleDesc': 'Skyscrapers also known as "Towers" is a logic puzzle with simple rules and challenging solutions.',
					'puzzleRules1': 'The rules are simple.\nThe objective is to place skyscrapers in all cells on the grid according to the rules:',
					'puzzleRulesTable': [
						'The height of the skyscrapers is from 1 to the size of the grid i.e. 1 to 4 for a 4x4 puzzle.',
						'You cannot have two skyscrapers with the same height on the same row or column.',
						'The numbers on the sides of the grid indicate how many skyscrapers would you see if you look in the direction of the arrow.',
						'Place numbers in each cell to indicate the height of the skyscrapers.',
					],
					'difficultyTable': [
						"4x4 Easy",
						"4x4 Normal",
						"4x4 Hard",
						"5x5 Easy",
						"5x5 Normal",
						"5x5 Hard",
						"6x6 Easy",
						"6x6 Normal",
						"6x6 Hard",
					],
				},

				'de': {
					'puzzleName': 'skyscrapers',
					'puzzleTitle': 'Skyscrapers',
					'puzzleDesc': 'Wolkenkratzer, auch bekannt als "Towers", ist ein Logikrätsel mit einfachen Regeln und herausfordernden Lösungen.',
					'puzzleRules1': 'Die Regeln sind einfach.\nZiel ist es, in allen Zellen des Rasters Wolkenkratzer gemäß den Regeln zu platzieren:',
					'puzzleRulesTable': [
						'Die Höhe der Wolkenkratzer reicht von 1 bis zur Größe des Rasters, d. h. 1 bis 4 für ein 4x4-Puzzle.',
						'Sie können nicht zwei Wolkenkratzer mit derselben Höhe in derselben Zeile oder Spalte haben.',
						'Die Zahlen an den Seiten des Rasters geben an, wie viele Wolkenkratzer Sie sehen würden, wenn Sie in Pfeilrichtung blicken.',
						'Tragen Sie Zahlen in jede Zelle ein, um die Höhe der Wolkenkratzer anzugeben.',
					],
					'difficultyTable': [
						"4x4 Easy",
						"4x4 Normal",
						"4x4 Hard",
						"5x5 Easy",
						"5x5 Normal",
						"5x5 Hard",
						"6x6 Easy",
						"6x6 Normal",
						"6x6 Hard",
					],
				}
			},
			'futoshiki': {
				'en': {
					'puzzleName': 'futoshiki',
					'puzzleTitle': 'Futoshiki',
					'puzzleDesc': 'Futoshiki also known as "More or Less" is a logic puzzle with simple rules and challenging solutions.',
					'puzzleRules1': 'The rules are simple.\nYou have to fill the grid with numbers so that:',
					'puzzleRulesTable': [
						'The numbers are from 1 to the size of the grid i.e. 1 to 5 for a 5x5 puzzle.',
						'Each row and column must contain only one instance of each number.',
						'The numbers should satisfy the comparison signs - less than or greater than.',
						'For bigger puzzles the letters (A,B,C etc.) follow after the number 9.',
					],
					'difficultyTable': [
						"4x4 Easy",
						"5x5 Easy",
						"5x5 Normal",
						"5x5 Hard",
						"7x7 Easy",
						"7x7 Normal",
						"7x7 Hard",
						"9x9 Easy",
						"9x9 Normal",
						"9x9 Hard",
					],
				}
			}
		}