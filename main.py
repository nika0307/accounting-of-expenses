import PySimpleGui as sg 

sg.theme("DarkTanBlue")

options=[[sg.Frame('Choose your Expenses',[[sg.Radio('education and culture', 'rd_expenses', key='education and culture'),
sg.Radio('inceme','rd_expenses', key='inceme')
sg.Radio('food','rd_expenses', key='food')
sg.Radio('health and spents','rd_expenses', key='health and spents')
sg.Radio('inswrance and taxec','rd_expenses', key='inswrance and taxec')
sg.Radio('entertainment','rd_expenses', key='entertainment')
sg.Radio('other','rd_expenses', key='other')]], border_width=10)],

[sg.Frame('Choose your Currency', [[sg.Radio('USD','rd_expenses', key='USD')
sg.Radio('EUR','rd_expenses', key='EUR')
sg.Radio('UAH','rd_expenses', key='UAH')],

[sg.Frame('Choose your Analysis', [[sg.Radio('%','rd_expenses', key='%')
sg.Radio('currency','rd_expenses', key='currency')
                                    
 window.close()
