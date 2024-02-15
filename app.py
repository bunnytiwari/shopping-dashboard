import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns



st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")


df = pd.read_csv("C:/Users/shrad/OneDrive/Desktop/App/data/shopping_trends.csv")

selected=st.sidebar.radio('select one',["Data", "Charts", "summary"])

if selected=="Data":
    st.title("SHOPPING WORLD ")
    st.image("ssss.jpg")
    st.title("DATA Description")
    st.markdown("This dataset encompasses various features related to customer shopping preferences, gathering essential information for businesses seeking to enhance their understanding of their customer base. The features include customer age, gender, purchase amount, preferred payment methods, frequency of purchases, and feedback ratings. Additionally, data on the type of items purchased, shopping frequency, preferred shopping seasons, and interactions with promotional offers is included. With a collection of 3900 records, this dataset serves as a foundation for businesses looking to apply data-driven insights for better decision-making and customer-centric strategies")
    st.subheader("DATA")
    df = pd.read_csv("C:/Users/shrad/OneDrive/Desktop/App/data/shopping_trends.csv")
    df
    st.image("jjj.gif") 
    
if selected == "Charts":

    #----sidebar----
    Location = st.sidebar.multiselect(
        "select the Location:",
        options=df["Location"].unique(),
        default=df["Location"].unique()
    )
    


    Season = st.sidebar.multiselect(
        "select the Season:",
        options=df["Season"].unique(),
        default=df["Season"].unique()
    )


    Gender = st.sidebar.multiselect(
        "select the Gender:",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
    )
    

    Age_grp = st.sidebar.multiselect(
        "select the Age_grp:",
        options=df["Age_grp"].unique(),
        default=df["Age_grp"].unique()
    )


    df_selection = df.query(
        "Location == @Location & Season & Age_grp & Gender == @Gender"
    )

    #---- MAINPAGE ----
    st.title(":bar_chart: SALES DASHBOARD")
    st.markdown("##")

    #TOP KPI'S
    total_sales = int(df_selection["Purchase Amount (USD)"].sum())
    average_rating = round(df_selection["Review Rating"].mean(),1)
    star_rating = ":star:" * int(round(average_rating,0))
    average_sale_by_transaction = round(df_selection["Purchase Amount (USD)"].mean(),2)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("total_sales")
        st.subheader(f"US $ {total_sales:,}")
    with middle_column:
        st.subheader("Average Rating:")
        st.subheader(f"{average_rating}{star_rating}")
    with right_column:
        st.subheader("Average Sales Per Transaction")
        st.subheader(f"US {average_sale_by_transaction}")

    st.markdown("---")




    #sales by product line
    col1,col2=st.columns(2)
    with col1:


    
        sales_by_Category = (
            df_selection.groupby(by=["Category"]).sum()[["Purchase Amount (USD)"]]
         )
    
   
   
        fig_product_sales = px.bar(
            sales_by_Category,
            x="Purchase Amount (USD)",
            y=sales_by_Category.index,
            orientation="h",
            title="<b>sales by Category</b>",
            color_discrete_sequence=["#ff0000"] * len(sales_by_Category),
            template="plotly_white"
        
        )
        st.plotly_chart(fig_product_sales)

    with col2:

        #sales by product line

        sales_by_Payment_Method = (
            df_selection.groupby(by=["Payment Method"]).sum()[["Purchase Amount (USD)"]]
        
        )
    

        fig_product_sale = px.bar(
            sales_by_Payment_Method,
            x="Purchase Amount (USD)",
            y=sales_by_Payment_Method.index,
            title="<b>sales by Payment Method</b>",
            color_discrete_sequence=["#ff0000"] * len(sales_by_Payment_Method),
            template="plotly_white"

        )
    

        st.plotly_chart(fig_product_sale)
    #----chart ----
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("Purchase Amount (USD) by Season and Item Purchase")
    data = {
        "Season": ["Spring", "Spring", "Summer", "Summer", "Fall", "Fall", "Winter", "Winter"],
        "Item Purchase": ["Item1", "Item2", "Item1", "Item2", "Item1", "Item2", "Item1", "Item2"],
        "Purchase Amount (USD)": [100, 150, 200, 250, 300, 350, 400, 450]
    }

    # Create DataFrame from data
    df = pd.DataFrame(data)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Season", y="Purchase Amount (USD)", hue="Item Purchase", data=df)
    plt.xlabel("Season")
    plt.ylabel("Purchase Amount (USD)")
    plt.legend(title="Item Purchase")
    plt.xticks(rotation=45)
    st.pyplot()

    #----bar chart----
    # Sample data
    data = {
       "Gender": ["Male", "Female", "Male", "Female", "Male"],
        "Payment Method": ["Credit Card", "PayPal", "Credit Card", "Credit Card", "PayPal"]
    }

    # Create a donut chart
    def create_donut_chart(data):
        gender_counts = {gender: data["Gender"].count(gender) for gender in set(data["Gender"])}
        payment_counts = {payment: data["Payment Method"].count(payment) for payment in set(data["Payment Method"])}

        fig = go.Figure(data=[go.Pie(labels=list(gender_counts.keys()), values=list(gender_counts.values()), hole=.3, name="Gender"),
                          go.Pie(labels=list(payment_counts.keys()), values=list(payment_counts.values()), hole=.6, name="Payment Method")])

        fig.update_layout(title="Distribution of Gender and Payment Method")
        return fig

    # Render the chart
    st.plotly_chart(create_donut_chart(data), use_container_width=True)
 
    data = {
        "Age_grp": ["18-25", "26-35", "36-45", "46-55", "56+"],
        "Purchase Amount (USD)": [100, 150, 200, 250, 300]
    }

    # Create DataFrame from data
    df = pd.DataFrame(data)

    # Plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x="Age_grp", y="Purchase Amount (USD)", data=df)
    plt.title("Purchase Amount by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Purchase Amount (USD)")
    plt.xticks(rotation=45)
    st.pyplot()


if selected == "summary":
    st.title("CONCLUSION:")
    
    st.subheader("sales by category")
    st.markdown("sales in clothing and accessories are more profitable.")
    st.subheader("sales_by_Payment_Method")
    st.markdown("People most preffered to pay by Credit Card")
    st.subheader("Purchase Amount (USD) by Season and Item Purchase")
    st.markdown("The Largest Purchase Amount is in Winter season ")
    st.subheader("purchase Amount by age")
    st.markdown("Above the Age of 40 they more like to do shoppings")   




    



    









    



























