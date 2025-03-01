from os import getenv

# Blueprint config
OFFERS_BLUEPRINT = "offers_microservice"
OFFERS_BLUEPRINT_PREFIX = "/offers"

# External routes
USERS_PATH = getenv("USERS_PATH", "http://localhost:5000")
USERS_ME_ROUTE = "/users/me"
