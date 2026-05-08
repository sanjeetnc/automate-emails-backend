from datetime import date
import pandas as pd
from sendemails import send_email

SHEET_ID = "14Y8r1qTXId9m2n36w_Zc2rTCUVJoqGdfBdLAkASQjSo"

URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"


def load_df(url):
    df = pd.read_csv(url)

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")
    df["reminder_date"] = pd.to_datetime(df["reminder_date"], format="%d-%b-%y")
    
    

    print(df.columns.tolist())

    return df


def query_data_send_mails(df):
    present = date.today()
    email_counter = 0

    for _, row in df.iterrows():

        if (present >= row["reminder_date"].date()) and (row["mailstatus"] == "no"):
            print(row["email"])
            print(type(row["email"]))
            send_email(
                receiver_email=row["email"],
                name=row["name"],
                subject="Daily Internship Report",
                date=row["Date"].date(),
                morning=row["morning"],
                prelunch=row["prelunch"],
                postlunch=row["postlunch"],
                reminder_date=row["reminder_date"].date().strftime("%d-%b-%y")
            )

            email_counter += 1

    return f"Total Emails Sent: {email_counter}"


df = load_df(URL)

result = query_data_send_mails(df)

print(result)