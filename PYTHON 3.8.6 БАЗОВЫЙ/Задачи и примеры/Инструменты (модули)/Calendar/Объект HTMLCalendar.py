""" Объект HTMLCalendar """

from calendar import HTMLCalendar

c = HTMLCalendar()

# Методы класса HTMLCalendar
# позволяют получать строку,
# содержащую календарные данные
# в формате HTML.
a = c.formatmonth(2020, 6)

print(a)
# <table border="0" cellpadding="0" cellspacing="0" class="month"> <tr><th colspan="7" class="month">June
# 2020</th></tr> <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th
# class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr> <tr><td
# class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td
# class="sat">6</td><td class="sun">7</td></tr> <tr><td class="mon">8</td><td class="tue">9</td><td
# class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td
# class="sun">14</td></tr> <tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td
# class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr> <tr><td
# class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td
# class="sat">27</td><td class="sun">28</td></tr> <tr><td class="mon">29</td><td class="tue">30</td><td
# class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td
# class="noday">&nbsp;</td></tr> </table>
