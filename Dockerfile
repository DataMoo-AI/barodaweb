# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:2.0.0
# Use subdirectory as working directory
WORKDIR /app
# Copy any additional custom requirements, if necessary (uncomment next line)
#COPY actions/requirements.txt ./
# Change back to root user to install dependencies
USER root
# Install extra requirements for actions code, if necessary (uncomment next line)
COPY . .

RUN pip install -r requirements.txt
#RUN pip install pymysql
# Copy actions folder to working directory
# By best practices, don't run the code with root user
USER 1001