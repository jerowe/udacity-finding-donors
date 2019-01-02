FROM node:10

RUN npm install -g @angular/cli

## Mount any volumes here and BUILD
RUN mkdir -p /app

WORKDIR /app

EXPOSE 4200

CMD ["/bin/bash", "-c", "npm install"]
