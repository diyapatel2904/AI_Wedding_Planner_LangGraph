FROM python:3.10
 
# Step 2: Set the working director inside the container
WORKDIR /app

# Step 3: Copy application code into the container
COPY . /app
COPY requirements.txt /app/

# Step 4: Install dependencie
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the application port
EXPOSE 8501
 
# Run the Streamlit app using -m pattern
CMD ["streamlit", "run", "app.py"]
