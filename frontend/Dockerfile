FROM node:14.17.3

WORKDIR /app  

COPY package*.json ./

RUN npm i -g @vue/cli
RUN npm install

CMD [ "npm", "run", "serve" ]

EXPOSE 8080