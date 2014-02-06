from klout import *

# Make the Klout object
k = Klout('epvjtgvg53rqz5pg5jwjz45b')
#users=["m_735_","Ghadeer__19","Invent_mx", "ArchHouseDeli", "MADD_skillzzz","karaage0212","1097_danilo","RUDENKO_OLGA", "aztekengold", "ShawnCheri", "AlenkaPylaeva", "florenciataly", "alialiali25ali", "aningrasin", "omgitsdiegoo_cx", "mo0onchildd", "hasmnews", "srtamelancolia", "mikimo_tan", "MartinaSus", "Abeer_411", "kadincaportal"]
# Get kloutId of the user by inputting a twitter screenName
#for i in users:
kloutId = k.identity.klout(screenName="RinzyRoo420").get('id')
print i
print kloutId
# Get klout score of the user
score = k.user.score(kloutId=kloutId).get('score')

print "User's klout score is: %s" % (score)

# By default all communication is not secure (HTTP). An optional secure parameter
# can be sepcified for secure (HTTPS) communication
k = Klout('epvjtgvg53rqz5pg5jwjz45b', secure=True)

# Optionally a timeout parameter (seconds) can also be sent with all calls
score = k.user.score(kloutId=kloutId, timeout=5).get('score')
