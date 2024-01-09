import pandas as pd

# Series
mountain_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])
print(mountain_height)

mountains = pd.Series( 
data=[2061, 2035.8, 2028.5, 2022.5, 2016.4], 
index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"], name="Height, m", 
dtype=float,
)
print(mountains)

# index
print(mountain_height[0]) # 2061.0
print(mountains["Goverla"]) # 2061.0
print(mountains[["Pip_Ivan", "Goverla", "Gutin_Tomnatik"]])
print(mountains[1:3])
print(mountains["Brebenskyl":"Petros"])
print(mountains.Petros) # 2022.5
print(mountains > 2030)
print(mountains[mountains > 2030])

print('Goverla' in mountains)

# sort
sort_index = mountains.sort_index()
print(sort_index)
mountains.sort_values(inplace=True, ascending=False)
print(mountains)

mountains_height = pd.Series( 
{"Goverla": 2061, "Brebenskyl": 2035.8, "Pip_Ivan": 2028.5}, 
index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"], name="Height, m", 
dtype=float,
)

print(mountains_height)

mountains_height.fillna(0, inplace=True)

print(mountains_height)


# DataFrame

contacts = pd.DataFrame(
  {
    "name": [
      "Allen Raymond",
      "Chaim Lewis",
      "Kennedy Lane",
      "Wylie Pope",
      "Cyrus Jackson",
    ],
    "email": [
      "nulla.ante@vestibul.co.uk",
      "dui.in@egetlacus.ca",
      "mattis.Cras@nonenimMauris.net",
      "est@utquamvel.net",
      "nibh@semsempererat.com",
    ],
    "phone": [
      "(992) 914-3792",
      "(294) 840-6685",
      "(542) 451-7038",
      "(692) 802-2949",
      "(501) 472-5218",
    ],
    "favorite": [False, False, True, False, True],
  },
  index=[1, 2, 3, 4, 5],
)

print(contacts)
print(contacts['email'])
print(contacts.loc[3]) #by val
print(contacts.iloc[4])
print(contacts[:2])
print(contacts[contacts['favorite']])

# read from file
users = pd.read_csv("users.csv")
print(users)

# write to file
contacts.to_csv("data.csv", index=False)
contacts.to_excel('contacts.xlsx', sheet_name='Contacts')

# json

json_str = {
  "name": {"1": "Michael", "2": "John", "3": "Liza"},
  "country": {"1": "Canada", "2": "USA", "3": "Australia"}
}
pd_data =pd.DataFrame(json_str)
pd_data.to_json("employees.json", orient="split")

