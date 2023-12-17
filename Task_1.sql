SELECT c.login, COUNT( o."inDelivery")
FROM "Orders" as "o"
INNER JOIN "Couriers" as "c" ON "o"."courierId" = "c"."id" where o."inDelivery" = true GROUP BY c.login;