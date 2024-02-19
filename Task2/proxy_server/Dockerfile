FROM nginx:latest

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom configuration file into the container
COPY nginx.conf /etc/nginx/conf.d/

# Expose port 80 outside the container
EXPOSE 80

# Command to start Nginx in the foreground when the container is launched
CMD ["nginx", "-g", "daemon off;"]





