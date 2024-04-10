FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install any necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    nginx

# Expose any ports the app is expecting
EXPOSE 80

# Start nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
