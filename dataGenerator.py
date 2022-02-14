from DataGenerator import *
from DataGenerator.Generators import *
from DataGenerator.Table import *
from DataGenerator.Column import *

db = Databases.Sqlite3DB()
db.connect("db.sqlite3")

user = Table("auth_user")
user.addColumns([
	Column("id", SerialGenerator(120), True),
	Column("password", ConstantGenerator("pbkdf2_sha256$260000$qNOQfRUbv97uZY8hsQmD6i$+Pl4VZlQQ2aLr9gxuJB5WyEQmKFS2PJHQlh/3l1pe04=")),
	Column("last_login", ConstantGenerator("2021-12-22 16:44:20.345568")),
	Column("is_superuser", ConstantGenerator(1)),
	Column("username", FakeUsernameGenerator()),
	Column("last_name", FakeLastNameGenerator()),
	Column("email", FakeEmailGenerator()),
	Column("is_staff", ConstantGenerator(1)),
	Column("is_active", ConstantGenerator(1)),
	Column("date_joined", ConstantGenerator("2021-12-17 11:41:18.278069")),
	Column("first_name", FakeFirstNameGenerator()),
])
games = Table("main_skyscraperspuzzle")
games.addColumn(Column("id", SerialGenerator(100), True))
playedGame = Table("main_playedgame")
playedGame.addColumns([
	Column("id", SerialGenerator(120), True),
	Column("date", FakeCurrentMonthDateTimeGenerator()),
	Column("time", PrettyTimeGenerator(1, 900)),
	Column("puzzle_id", SetGenerator(db.getPkSet(games))),
	Column("user_id", SetGenerator(db.getPkSet(user))),
])

# db.insertRows(user, 100)
db.wipeTable(playedGame)
db.insertRows(playedGame, 50000)
