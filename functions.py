def calc_gross(benefits,basic_salary):
 gross_salry= basic_salary+ benefits
 return gross_salry

basic_salary=float(input("Enter basic salary"))
benefits=float(input("Enterbenefits"))
grossslry=calc_gross(basic_salary,benefits)
print(grossslry)