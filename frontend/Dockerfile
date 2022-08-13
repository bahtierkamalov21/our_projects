# Pull official base image
FROM node:14.20.0

# Set work directory
WORKDIR /usr/src/app

# Set timezone
ENV TZ=Europe/Moscow

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project
COPY . .

EXPOSE 8080
