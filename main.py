import pickle
dummy_data = {"installed":{"client_id":{"installed":{"client_id":"253945389224-ap234k1b4ulh9vsc2ot3n9n0ss864ips.apps.googleusercontent.com","project_id":"ninjaprateek1","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"8zJkONr1eS7LD7lC-VjOEINZ","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}},"project_id":"ninjaprateek1","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"8zJkONr1eS7LD7lC-VjOEINZ","redirect_uris":{"client_id":"wow"}}}

a = open('results.txt','w')
write_data = []

def rec(dummy_data, depth):
    global write_data
    for k in dummy_data:
        if type(dummy_data[k]) == dict:
            write_data.append('\t'*depth + ' - ' + str(k)+'\n')

            rec(dummy_data[k],depth+1)
        else:
            write_data.append('\t'*depth + ' - ' + str(k)+'\n')
    

rec(dummy_data,0)

a.writelines(write_data)
a.close()