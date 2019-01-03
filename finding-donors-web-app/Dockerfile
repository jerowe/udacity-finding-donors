FROM node:10

RUN npm install -g @angular/cli@6.2.8

## Mount any volumes here and BUILD
RUN mkdir -p /app

WORKDIR /app

EXPOSE 4200

ENV NODE_ENV dev

CMD ["/bin/bash", "-c", "npm install; npm install --only=dev"]
