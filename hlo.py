command = ''
started = False
while True:
     command = input('>').lower()
     if command == 'help':
         print('''
start - To start the car
stop  - To stop the car
quit  - To exit
''')
     elif command == 'start':
       if started:
         print('car already started')
       else:
         started = True
         print('started the car')
     elif command == 'stop':
       if not started:
         print('car already stopped')
       else:
         started = False
         print('stop the car')
     elif command == 'quit':
         break
     else:
         print('i cannot understand')



