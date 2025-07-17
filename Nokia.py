phone_menu = """
		1. Phone book
		2. Messages
		3. Chat
		4. Call register
		5. Tones
		6. Settings
		7. Call divert
		8. Games
		9. Calculator
		10.Reminders
		11. Clock
		12. Profiles
		13. SIM services

		"""
print(phone_menu)
data = int(input("Select an option: "))
match data:
	case 1:
		print(	"""
					1. Search
					2. Service Nos.
					3. Add name
					4. Erase
					5. Edit
					6. Assign tone
					7. Send b'card
					8. Options
					9. Speed dials
					10.Voice tags

					""")
		
		data = int(input("Select an option: "))
		match data:
			case 1:
				print("Search")
			case 2:
				print("Service Nos.")
			case 3:
				print("Add name")
			case 4:
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Assign tone")
			case 7:
				print("Send b'card")
			case 8:
				print("""
					1. Type of view
					2. Memory status
				
				""")
			case 9:
				print("Speed dials")
			case 10:
				print("Voice tags")
	case 2:
		print(""" 
			1. Write messages
			2. Inbox
			3. Outbox
			4. Picture messages
			5. Templates
			6. Smileys
			7. Message settings
			8. Info service
			9. Voice mailbox number
			10. Service command editor

			""")

		data = int(input("Select an option: "))
		match data:
			case 1:
				print("Write messages")
			case 2:
				print("Inbox")
			case 3: 
				print (Output)
			case 4:
				print("Picture messages")
			case 5:
				print("Templates")
			case 6:
				print("Smileys")
			case 7:
				print (""" 
					1. Set
					2. Common
				
					""")
	 
				message_settings = int(input("Select an option: "))
				match message_settings:
					case 1 : 
						print("""
					1. Message centre number
					2. Messages sent as
					3. Message validity

					 	""")
					case 2:
						print(""" 
					1. Delivery report
					2. Reply via same centre
					3. Character support				
					
						""")
		
	case 3:
		print("Chat")
	case 4:
		print(""" 
			1. Missed calls
			2. Received calls
			3. Dialled numbers
			4. Erase recent call lists
			5. Show call duration
			6. Show call costs
			7. Call cost settings
			8. prepaid credit


			""")
		calls = int(input("Select an option: "))
		match calls:
			case 1:
				print("Missed calls")
			case 2:	
				print("Received calls")
			case 3:
				print("Dialled numbers")
			case 4:
				print("Erase recent call lists")
			case 5: 
				print(""" 
					1. Last call duration
					2. All calls' duration
					3. Received calls' duration
					4. Dialled calls' duration;
					5. Clear timers
					
					""")
		
			case 6:
				print("""
					1. Last call cost
					2. All calls' cost
					3. Clear counters
	
 					""")
			case 7:
				print(""" 
					1. Call cost limit
					2. Show costs in
			
					""")
			case 8: 
				print("Prepaid credit")	
			

	case 5:
		print(""" 
			1. Ringing tone
			2. Ringing volume
			3. Incoming call alert
			4. Composer
			5. Message alert tone
			6. Keypad tones
			7. Warning and game tones
			8. Vibrating alert
			9. Screen saver


			""")
	case 6:
		print("""
			1. Call settings
			2. Phone settings
			3. Security settings
			4. Restore factory settings
			

			 """)
		settings = int(input("Select an option: "))
		match settings:
				case 1:
					print(""" 
						1. Authomatic redial
						2. Speed dialling
						3. Call waiting options
						4. Own number sending
						5. Phone line in use
						6. Automatic answer

						""")
				case 2:
					print(""" 
						1. Language
						2. Cell info display
						3. Welcome note
						4. Network selection
						5. Lights
						6. Confirm SIM service actions
					

						""")
				case 3:
					print(""" 
						1. PIN code request
						2. Call barring service
						3. Fixed dialling
						4. Closed user group
						5. Phone security
						6. Change access codes


						""")

	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		print(""" 
			1. Alarm clock
			2. Clock settings
			3. Date setting
			4. Stopwatch
			5. Countdown timer
			6. Auto update of time and date
			
			""")
	case 12:
		print("Profiles")
	case 13:
		print("SIM services")

