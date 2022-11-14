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

CREATE TABLE
  "cart" (
    FOREIGN KEY ("user_id") REFERENCE "users" ("id"),
    FOREIGN KEY ("item_id") REFERENCE "items" ("id"),
    FOREIGN KEY ("item_amount") REFERENCE "items" ("amount"),
  );
