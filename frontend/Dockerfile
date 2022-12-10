FROM node:18.7.0

WORKDIR /app

EXPOSE 3000

COPY package.json package-lock.json ./

RUN npm install --silent
RUN npm run lint-fix
COPY . ./

CMD ["npm","start"]
