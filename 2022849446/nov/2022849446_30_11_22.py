from urllib.request import urlopen
import urllib.error
# import twurl
import json
import sqlite3
import ssl

# def presentationCode_1():
    #use twurl
    # TWTTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # conn = sqlite3.connect('spider.sqlite')
    # cur = conn.cursor()

    # cur.execute('''
    #             CREATE TABLE IF NOT EXISTS Twitter
    #             (name TEXT, retrieved INTEGER, friends INTEGER)''')

    # # Ignore SSL certificate errors
    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE

    # while True:
    #     acct = input('Enter a Twitter account, or quit: ')
    #     if (acct == 'quit'): break
    #     if (len(acct) < 1):
    #         cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
    #         try:
    #             acct = cur.fetchone()[0]
    #         except:
    #             print('No unretrieved Twitter accounts found')
    #             continue
            
    #     url = twurl.augment(TWTTER_URL,
    #                         {'screen_name': acct, 'count': '5'})
    #     print('Retrieving', url)
    #     connection = urlopen(url, context=ctx)
    #     data = connection.read().decode()
    #     headers = dict(connection.getheaders())
        
    #     print('Remaining', headers['x-rate-limit-remaining'])
    #     js = json.loads(data)
    #     #debugging
    #     #print(json.dumps(js, indent=4))
        
    #     cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))
        
    #     countnew = 0
    #     countold = 0
    #     for u in js['users']:
    #         friend = u['screen_name']
    #         print(friend)
    #         cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
    #                     (friend, ))
    #         try:
    #             count = cur.fetchone()[0]
    #             cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
    #                         (count+1, friend))
    #             countold = countold + 1
    #         except:
    #             cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
    #                         VALUES (?, 0, 1)''', (friend, ))
    #             countnew = countnew + 1
    #     print('New accounts=',countnew,' revisited=',countold)
    #     conn.commit()
        
    # cur.close()
    
def presentationCode_2():
    conn = sqlite3.connect('music.sqlite')
    cur = conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS Tracks')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
    
    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
                ('Thunderstruck', 20))
    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
                ('My Way', 15))
    conn.commit()
    
     # Debugging
    print('Tracks:')
    cur.execute('SELECT title, plays FROM Tracks')
    for row in cur:
        print(row)
        
    cur.execute('DELETE FROM Tracks WHERE plays < 100')
    
    # Debugging
    print('Tracks:')
    cur.execute('SELECT title, plays FROM Tracks')
    for row in cur:
        print(row)
    
    conn.commit()
    
    cur.close()

def main():
    print("Student id is:", 2022849446)

    presentationCode_2()


if __name__ == "__main__":
    main()
