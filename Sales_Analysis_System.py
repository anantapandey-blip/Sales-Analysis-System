import numpy as np
password= 567890
name= "Ananta Pandey"
print("\n --------------------- Sales Analysis System --------------------------\n ")

sales_info = np.array([["Products", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"],
                       ["Biscuits",   5489   ,     956    ,    5489  ,   2234   ,   1189  ,    267    ,  8235],
                       ["Milk Cakes" , 7890   ,     6645    ,   4567  ,    2123  ,   2367  ,    5285  ,   2276],
                       ["Noodles"  ,  3489   ,     3467    ,   889    ,    535   ,   136    ,   426  ,   978 ],
                       ["Dry Fruits", 525    ,     889    ,     687    ,    156    ,   334    ,   8856 , 7843],
                       ["Butter"    , 4565   ,     5690    ,    498    ,    1345   ,   770    ,    890  , 478]])
try:
    password_input= int(input("Enter the Password : "))
    if password_input!=password:
       print("Wrong Password")
       exit
    else:
       print("Successfully Login!")
       print(f"\n-------------- Welcome {name} ----------------")


except ValueError:
   print(" Please enter a valid number ")
   

while True:
    menu= input("\n 1. Total Sale  \n 2. Weekly Sale   \n 3. Product vise sale \n 4. Exit \n  ")
    if menu=="1":
        total_sale = sales_info[1:,1:].astype(int)
        total= np.sum(total_sale)
        print(f"Total sales of worth ₹ {total} ")

    elif menu=="2":
        user_input=input("Enter the week:- ").strip().title()
        days= sales_info[0, 1:]
        week_sale= np.where(days == user_input)[0]
        if len(week_sale) == 0:
            print("Day not found!")

        else:
            day_index= week_sale[0]

            daily_sales= np.sum(
               sales_info[1:, day_index + 1].astype(int)

            )
            print(f"{user_input} sales : ₹ {daily_sales}")

    elif menu=="3":
        user_input=input("Enter the Product:- ").strip().title()
        product = sales_info[1:, 0]
        product_sale= np.where(product == user_input)[0]
        if len(product_sale) ==0:
          print("Product not found!")
        
        else:
         product_sale = product_sale[0]
        
         products_sales = np.sum(
            sales_info[product_sale + 1 , 1: ].astype(int)
        
             )
        print(f"{user_input} sales : ₹ {product_sale}")



    elif menu=="4":
       user_input= input("Do you want to exit?(yes/no)")
       if user_input=="yes":
          print("Exiting..........")
          break
       else:
          continue

    