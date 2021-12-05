class Localization:
	def __init__(self):
		self.content = {
			'skyscrapers': {
				'en': {
					'puzzleDesc': 'Skyscrapers also known as "Towers" is a logic puzzle with simple rules and challenging solutions.',
					'puzzleRules1': 'The rules are simple.\nThe objective is to place skyscrapers in all cells on the grid according to the rules:',
					'puzzleRulesTable': [
						'The height of the skyscrapers is from 1 to the size of the grid i.e. 1 to 4 for a 4x4 puzzle.',
						'You cannot have two skyscrapers with the same height on the same row or column.',
						'The numbers on the sides of the grid indicate how many skyscrapers would you see if you look in the direction of the arrow.',
						'Place numbers in each cell to indicate the height of the skyscrapers.',
					],
				},

				'de': {
					'puzzleDesc': 'Wolkenkratzer, auch bekannt als "Towers", ist ein Logikrätsel mit einfachen Regeln und herausfordernden Lösungen.',
					'puzzleRules1': 'Die Regeln sind einfach.\nZiel ist es, in allen Zellen des Rasters Wolkenkratzer gemäß den Regeln zu platzieren:',
					'puzzleRulesTable': [
						'Die Höhe der Wolkenkratzer reicht von 1 bis zur Größe des Rasters, d. h. 1 bis 4 für ein 4x4-Puzzle.',
						'Sie können nicht zwei Wolkenkratzer mit derselben Höhe in derselben Zeile oder Spalte haben.',
						'Die Zahlen an den Seiten des Rasters geben an, wie viele Wolkenkratzer Sie sehen würden, wenn Sie in Pfeilrichtung blicken.',
						'Tragen Sie Zahlen in jede Zelle ein, um die Höhe der Wolkenkratzer anzugeben.',
					],
				},

				'fr': {
					'puzzleDesc': 'Les gratte-ciels également connus sous le nom de « tours » sont un casse-tête logique avec des règles simples et des solutions difficiles.',
					'puzzleRules1': "Les règles sont simples.\nL'objectif est de placer des gratte-ciel dans toutes les cellules de la grille selon les règles:",
					'puzzleRulesTable': [
						'La hauteur des gratte-ciel est de 1 à la taille de la grille soit 1 à 4 pour un puzzle 4x4.',
						'Vous ne pouvez pas avoir deux gratte-ciel de même hauteur sur la même ligne ou colonne.',
						'Les chiffres sur les côtés de la grille indiquent combien de gratte-ciel verriez-vous si vous regardiez dans la direction de la flèche.',
						'Placez des nombres dans chaque cellule pour indiquer la hauteur des gratte-ciel.',
					],
				},

				'ru': {
					'puzzleDesc': 'Neboskreby, takzhe izvestnyye kak «Bashni», predstavlyayut soboy logicheskuyu golovolomku s prostymi pravilami i slozhnymi resheniyami',
					'puzzleRules1': "Pravila prosty.\nTsel' sostoit v tom, chtoby razmestit' neboskreby vo vsekh yacheykakh setki v sootvetstvii s pravilami",
					'puzzleRulesTable': [
						"Vysota neboskrebov ot 1 do razmera setki, to yest' ot 1 do 4 dlya golovolomki 4kh4.",
						"V odnoy stroke ili stolbtse ne mozhet byt' dvukh neboskrebov odinakovoy vysoty.",
						"Tsifry po storonam setki pokazyvayut, skol'ko neboskrebov vy uvidite, yesli posmotrite v napravlenii strelki.",
						"Pomestite chisla v kazhduyu yacheyku, chtoby ukazat' vysotu neboskrebov.",
					],
				},

				'extra': {
					'puzzleTitle': 'Skyscrapers',
					'puzzleName': 'skyscrapers',
					'difficultyTable': [
						{"id": 0, "text": "4x4 Easy"},
						{"id": 1, "text": "4x4 Normal"},
						{"id": 2, "text": "4x4 Hard"},
						{"id": 3, "text": "5x5 Easy"},
						{"id": 4, "text": "5x5 Normal"},
						{"id": 5, "text": "5x5 Hard"},
						{"id": 6, "text": "6x6 Easy"},
						{"id": 7, "text": "6x6 Normal"},
						{"id": 8, "text": "6x6 Hard"},
					],
				}
			},
			'futoshiki': {
				'en': {
					'puzzleTitle': 'Futoshiki',
					'puzzleDesc': 'Futoshiki also known as "More or Less" is a logic puzzle with simple rules and challenging solutions.',
					'puzzleRules1': 'The rules are simple.\nYou have to fill the grid with numbers so that:',
					'puzzleRulesTable': [
						'The numbers are from 1 to the size of the grid i.e. 1 to 5 for a 5x5 puzzle.',
						'Each row and column must contain only one instance of each number.',
						'The numbers should satisfy the comparison signs - less than or greater than.',
						'For bigger puzzles the letters (A,B,C etc.) follow after the number 9.',
					],
				},

				'extra': {
					'puzzleName': 'futoshiki',
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