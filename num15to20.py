





def calc_gross_salary(basic_salary, benefits):
    gross_salary=basic_salary+benefits
    return gross_salary

basic_salary=int(input("enter your basic salary: "))
benefits=int(input("enter your benefits: "))
gross_salary=calc_gross_salary(basic_salary,benefits)
print(f"nhif{gross_salary}")
# 15.NHIF
def calc_nhif( gross_salary):
    if gross_salary<5999:
        nhif=150
    elif gross_salary<7999:
        nhif=300
    elif gross_salary<11999:
        nhif=400
    elif gross_salary<14999:
        nhif=500
    elif gross_salary<19999:
        nhif=600
    elif gross_salary<24999:
        nhif=750
    elif gross_salary<29999:
        nhif=850
    elif gross_salary<34999:
        nhif=900
    elif gross_salary<39999:
        nhif=950
    elif gross_salary<44999:
        nhif=1000
    elif gross_salary<49999:
        nhif=1100
    elif gross_salary<59999:
        nhif=1200
    elif gross_salary<69999:
        nhif=1300
    elif gross_salary<79999:
        nhif=1400
    elif gross_salary<89999:
        nhif=1500
    elif gross_salary<99999:
        nhif=1600
    else:
        nhif=1700

    return nhif

nhif=calc_nhif(gross_salary)
print(nhif)
    
    
    
    
    # 16
    

def calc_nssf(a,b=0.06):
    if (a>0 and a<=18000):
        nsff=a*b
    else:
        nsff=18000*b
    return nsff

nssf=calc_nssf(gross_salary)
print(f"nssf: {nssf}")


# 17
def  calc_NHDF(grossslry):
    NHDF=grossslry * 0.015
    return NHDF
NHDF=calc_NHDF( gross_salary )
print(f"NHDF: {NHDF}")
    

# 18
def calc_taxable_income(grossslry,nssf,NHDF):
    taxable_income =grossslry -(nssf + NHDF)
    return taxable_income
taxable_income=calc_taxable_income(gross_salary,nssf,NHDF)
print(f"taxable_income: {taxable_income}")


# 19
def calc_payee(taxable_income):
    if (taxable_income >0 and taxable_income <= 24000):
        payee=taxable_income * 0.1
    elif (taxable_income >24000 and taxable_income<=32333):
        payee =taxable_income-24000 * 0.25 +24000 * 0.1
    else:
        payee=taxable_income-32333 * 0.3 +24000 * 0.1+8333*0.25
    return payee
payee=calc_payee(taxable_income)
print(f"payee: {payee}")



            # 20
def calc_net_salary(grossslry,nhif,NHDF,nssf,payee):
    net_salary= grossslry - (nhif + NHDF + nssf + payee)
    return net_salary
net_salary=calc_net_salary(gross_salary,nhif,NHDF,nssf,payee)
print(f"net salary: {net_salary}")