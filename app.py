 
import pickle
import streamlit as st

pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
def prediction(age,sex,chest_pain_type,bp_level,chol_level,fasting_blood_sugar):   
     
    if sex == "Male":
        sex = 0
    else:
        sex = 1

    if chest_pain_type  == "High":
        chest_pain_type = 3
    elif chest_pain_type  == "Normal":
        chest_pain_type = 2
    elif chest_pain_type  == "Low":
        chest_pain_type = 1
    else:
        chest_pain_type = 0

    
    if fasting_blood_sugar =="Low":
        fasting_blood_sugar = 0
    else:
        fasting_blood_sugar = 1
 
    # Making predictions 
    prediction = classifier.predict([[age,sex,chest_pain_type,bp_level,chol_level,fasting_blood_sugar]])
     
    if prediction==0:
        import webbrowser
        f = open('file1.html','w')
        message = """<html>
        <head><h1 style="text-align:center">Your health is normal,Recently there is a No Risk</h1></head>
        <body>
        <h2>Diet You need to follow</h2>
        <ul>
        <li>Eat a wide variety of foods from the five food groups: plenty of colourful vegetables, legumes/beans; fruit; grain (cereal) foods, mostly wholegrain and high fibre varieties; lean meats and poultry, fish, eggs, tofu, nuts and seeds; milk, yoghurt, cheese or their alternatives, mostly reduced fat.Drink plenty of water – six to eight cups of fluid per day.</li>
        <li>Limit foods high in saturated fat, such as biscuits, cakes, pastries, pies, processed meats, commercial burgers, pizza, fried foods, potato chips, crisps and other savoury snacks.</li> 
        <li>Replace high fat foods containing mostly saturated fat with foods containing mostly polyunsaturated and monounsaturated fats. Swap butter, cream, cooking margarine, coconut and palm oil with unsaturated fats from oils, spreads, nut butters and pastes, and avocado.</li>
        <li>Limit foods and drinks containing added salt, and don’t add salt to foods in cooking or at the table.</li>
        <li>Limit foods and drinks containing added sugars, such as confectionery, sugar-sweetened soft drinks and cordials, fruit drinks, vitamin waters, energy and sports drinks.</li>
        <li>Limit alcohol. (Drink no more than two standard drinks a day.)</li>
        <li>Keep ‘extras’ or ‘sometimes foods’ to a minimum – they’re not a regular part of a healthy diet. Extras are the high sugar, high fat, high salt foods listed above, such as commercial burgers, pizza, alcohol, lollies, cakes and biscuits, fried foods, and fruit juices and cordials. </li>
        <li>Be physically active. (Aim for at least 30 minutes of moderate intensity physical activity, such as walking, every day.)</li>
        </ul>
        <h2>Exercises to keep healthy</h2>
        <ul>
        <li>Water aerobics</li>
        <li>Chair yoga</li>
        <li> Resistance band workouts</li>
        <li>Pilates</li>
        <li>Walking</li>
        <li>Body weight workouts</li>
        <li>Dumbbell strength training</li>
        </ul>
        
        <h2>Exercises Seniors Should Avoid</h2>
        <ol>
        <li>Squats with dumbbells or weights</li>
        <li>Bench press</li>
        <li>Leg press</li>
        <li>Long-distance running</li>
        <li>Abdominal crunches</li>
        <li>Upright row</li>
        <li>High-intensity interval training</li>
        </ol>
        </body>
        </html>"""
        f.write(message)
        f.close()
        return webbrowser.open_new_tab('file1.html')
    else:
        import webbrowser
        f = open('file2.html','w')
        message = """<html>
        <head><h1 style="text-align:center">You need to take care of yourself,recently there is a risk of heart disease</h1></head>
        <body>
        <h2>Diet You need to follow </h2>
        <ul>
        <li>Fill half your plate with fruits and vegetables. A quarter gets lean protein like baked fish, beans, or chicken. The last quarter holds grains, preferably whole, like brown rice.</li>
        <li>Caffeine can raise your blood sugar and blood pressure. If you have higher blood sugar or blood pressure after drinking coffee, “limit your caffeine intake to 200 milligrams -- about 2 cups of coffee -- a day,”</li>
        <li>Since you have high blood pressure, you should get no more than 1,500 milligrams of sodium per day. That's less than a teaspoon.So retrain taste buds. Instead of reaching for the saltshaker, flavor food with citrus zest, garlic, rosemary, ginger, jalapeno peppers, oregano, or cumin.Cooking at home also helps. “If you’re eating something from a bag or box or off a restaurant menu, chances are you’re getting too much sodium,”So avoid this.</li>
        <li>Look for visible seeds and grains in your food,Whole grains are rich in vitamins and minerals, plus contain fiber, which keeps you full and helps steady blood sugar. Aim for three to five servings of grains each day, and make at least half of those servings whole grains.</li>
        <li>Bananas are a good source of potassium. So are cantaloupe, broccoli, raw carrots, lentils, potatoes, whole wheat bread, bran flakes, and nuts.“Potassium naturally reduces the effects of sodium, helping to control blood pressure,”</li>
        <li>Favor fats from plant foods. Some options: olive oil, avocado, nuts, and flaxseed.Saturated fats, like you find in skin-on chicken, butter, and cheese, should make up less than 10% of your daily calories.Avoid trans fats -- the partially hydrogenated oils found in fried foods and baked goods. And limit saturated fats, which are mostly found in fatty cuts of meat and whole-fat dairy products. “Both of these unhealthy fats are linked to increased cholesterol, which contributes to heart disease,”</li>
        </ul>
        
        <h2>Exercises to keep healthy</h2>
        <ul>
        <li>Go for a nice run or jog</li>
        <li>Take a brisk walk</li>
        <li>Take a few laps at the pool</li>
        <li>Lift a few weights</li>
        <li>Strike a few yoga poses</li>
        <li>Ride a Bike</li>
        <li>Hit the Gym</li>
        </ul>
        
        <h2>Exercises Seniors Should Avoid</h2>
        <ol>
        <li>Squats with dumbbells or weights</li>
        <li>Bench press</li>
        <li>Leg press</li>
        <li>Long-distance running</li>
        <li>Abdominal crunches</li>
        <li>Upright row</li>
        <li>High-intensity interval training</li>
        </ol>
        
        </body>
        </html>"""
        f.write(message)
        f.close()
        return webbrowser.open_new_tab('file2.html')

      
def main():       
    html_temp = """ 
    <div style ="background-color:yellow;padding:12px"> 
    <h1 style ="color:black;text-align:center;">Helping Sunita For Living Healthier Life</h1> 
    </div> 
    """
      
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    age = st.number_input('Age of Women')
    sex = st.selectbox('Sex',("Male","Female")) 
    chest_pain_type = st.selectbox('chest pain type',("High","Normal","Low","No pain")) 
    bp_level = st.number_input("Enter the value of Blood Pressure Check-up ")
    chol_level = st.number_input("Enter the value of cholestrol Check-up ") 
    fasting_blood_sugar = st.selectbox('Blood Sugar',("Low","High")) 
         
    if st.button("Good to go"): 
        result = prediction(age,sex,chest_pain_type,bp_level,chol_level,fasting_blood_sugar) 
        
if __name__=='__main__': 
    main()
