# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



'''Durbin-Watson test'''

#print(melted_df.head(5))


'''fig5 = px.scatter(new_df, x='Coverage', y="Value",
    	         size="Value", color="AreaName",
                     hover_name="OdName", log_x=True, size_max=60)

st.plotly_chart(fig5, use_container_width=True)'''

#,title=f'Pie Chart for Year {selected_year}'



st.map(filtered_df,
    latitude='latitude',
    longitude='longitude',
    size='OdName',
    color='OdName')