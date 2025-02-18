import streamlit as st
import pandas as pd
import os
from io import BytesIO

#  set up our App

st.set_page_config(page_title='Data Sweeper', layout='wide')
st.title('📀 Data Sweeper')
st.write('Transfrom Your files between CSV and Excel Formats with built-in data\
cleaning and visualization')


upload_files = st.file_uploader('Upload your files (csv or Excel):', type=["csv", 'xlsx'],
                                accept_multiple_files=True)

if upload_files:
    for file in upload_files:
        files_ext = os.path.splitext(file.name)[-1].lower()

        if files_ext == '.csv':
            df = pd.read_csv(file)
        elif files_ext == '.xlsx':
            df = pd.read_excel(file)
        else:
            st.error(f'Unsupported file type : {files_ext}')
            continue

    # Display info about the file
    st.write(f'**File Name : ** {file.name}')
    st.write(f'**File Size : **{file.size/1024}')

    # Show 5 rowa of data
    st.write('🔍Preview the Head of DataFrame')
    st.dataframe(df.head())
    
    # Options for data cleaning
    st.subheader("Data Cleaning Options")
    if st.checkbox(f'clean Data for {file.name}'):
        col1 , col2 = st.columns(2)

        with col1:
            if st.button(f'Remove Duplicates from {file.name}'):
                df.drop_duplicates(inplace=True)
                st.write('Duplicates Removes!')
                
        with col2:
            if st.button(f'Fill Missing Values for {file.name}'):
                numeric_cols = df.select_dtypes(include=('number')).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write('Missing Values have been Filled!')
                
    # choose Specific cloumbs to keep or convert 
    st.subheader('Select Cloumns to convert')
    columns = st.multiselect(f'choose Columbs for {file.name}' , df.columns , default=df.columns)
    df = df[columns]
    
    # Create Some Visualizations
    st.subheader('📊 Data Visualization')
    if st.checkbox(f'Show Visualizarion for {file.name}'):
        st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
        
    # Convert the file -> to Excel
    st.subheader('Convertion Options')
    conversion_type = st.radio(f'Convert {file.name} to : ' , ['Csv' , "Excel"] , key=file.name) 
    if st.button(f'Convert {file.name}'):
        buffer = BytesIO()
        if conversion_type == "CSV":
            df.to_csv(buffer , index=False)
            file_name = file.name.replace(files_ext,'.csv')
            mime_type = 'text/csv'
            
        elif conversion_type == "Excel":
            df.to_csv(buffer , index=False)
            file_name = file.name.replace(files_ext,'.xlxs')
            mime_type = ''
        buffer.seek(0)
        
        
        # Download Button
        st.download_button(
            label=f'Downlaod {file.name} as {conversion_type}',
            data= buffer,
            file_name = file_name,
            mime=mime_type
        )
        
st.success('🎉All Files Proccesd!')
        
    
            
    