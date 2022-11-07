CREATE TABLE
  "users" (
    "id" INTEGER,
    "username" TEXT NOT NULL,
    "pwd" TEXT NOT NULL,
    PRIMARY KEY ("id" AUTOINCREMENT)
  );

CREATE TABLE
  "items" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "amount" INTEGER,
    PRIMARY KEY ("id" AUTOINCREMENT)
  );
