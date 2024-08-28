CREATE TABLE "client" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "email" varchar,
  "phone" varchar,
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE "sale" (
  "id" SERIAL PRIMARY KEY,
  "client_id" integer,
  "car_id" integer,
  "dealer_id" integer,
  "price" integer,
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE "car" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "price" integer
);

CREATE TABLE "dealer" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "address" varchar,
  "contact" varchar,
  "password" varchar
);

ALTER TABLE "sale" ADD FOREIGN KEY ("client_id") REFERENCES "client" ("id");

ALTER TABLE "sale" ADD FOREIGN KEY ("car_id") REFERENCES "car" ("id");

ALTER TABLE "sale" ADD FOREIGN KEY ("dealer_id") REFERENCES "dealer" ("id");


INSERT INTO dealer (name, address, contact, password) VALUES
('Wolfsvagen Rio Pequeno', 'Rua Vice Presidente Vagras 132', 'wlfs@gmail.com', '123'),
('Filhat Rio Pequeno', 'Rua Segundo de Maio 777', 'fht@gmail.com', '123'),
('Flord Rio Pequeno', 'Vice Almirante Arbeu 982', 'flrd@gmail.com', '123');

INSERT INTO car (name, price) VALUES
('Goul', 10000),
('Paulio', 12000),
('Finiesta', 20000);
