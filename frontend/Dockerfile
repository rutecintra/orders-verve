# Estágio de construção
FROM node:22-alpine as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
#RUN npm run build -- --configuration=production
RUN npm run build

# Estágio de produção
FROM nginx:1.25-alpine
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
