# Cloud Native Tooling Project

[![deploy](https://github.com/charity1475/python-helloworld/actions/workflows/docker-build.yml/badge.svg)](https://github.com/charity1475/python-helloworld/actions/workflows/docker-build.yml)

## Overview

This project is a Cloud Native Tooling exercise demonstrating a deployment pipeline from GitHub to Docker Hub. The process is automated using GitHub Actions workflows. The ultimate goal is to deploy a Docker image on a Kubernetes cluster using Argo CD and Helm charts, exposing services in the cluster.

## Workflow

1. **GitHub Actions:**
   - The CI/CD pipeline is triggered automatically on each push to the repository.
   - View the build status and details [here](https://github.com/charity1475/python-helloworld/actions/workflows/docker-build.yml).

2. **Docker Build and Push:**
   - GitHub Actions builds a Docker image from the Python Hello World application.
   - The built image is then pushed to Docker Hub for easy accessibility.

3. **Kubernetes Deployment with Argo CD:**
   - Argo CD is employed to automate the deployment process to a Kubernetes cluster.
   - Helm charts are used to define the application's configuration and deployment.

4. **Service Exposure:**
   - After successful deployment, services are exposed within the Kubernetes cluster, making the application accessible.

## Argo CD Manifest

![argocd](https://user-images.githubusercontent.com/58939045/123279199-4e03d880-d510-11eb-86ee-e68e01a5b5e4.png)

The provided Argo CD manifest includes the necessary configurations for deploying and managing the Python Hello World application within your Kubernetes cluster.

## Usage

1. **GitHub Actions:**
   - Monitor the CI/CD pipeline status on the [Actions tab](https://github.com/charity1475/python-helloworld/actions).

2. **Argo CD Deployment:**
   - Ensure you have Argo CD installed in your Kubernetes cluster.
   - Apply the provided Argo CD manifest to initiate the deployment.

3. **Accessing the Application:**
   - Once deployed, access the Python Hello World application through the exposed services in your Kubernetes cluster.

## Contributing

Contributions and feedback are welcome! If you encounter issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the sections based on the specifics of your project and provide additional details if necessary. Ensure that your README includes sufficient information for users to understand the purpose of the project, how to use it, and how to contribute.
