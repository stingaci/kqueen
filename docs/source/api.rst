swagger: "2.0"

info:
  version: "0.1"
  title: Kubernetes Queen API
  description: A simple API to interact with Kubernetes clusters

schemes:
  - https
  - http

basePath: /api/v1

definitions:
  Service:
    type: object
    properties:
      id:
        type: "string"
        format: "uuid"
      name:
        type: "string"
      provisioner:
        type: "string"
        format: "uuid"
      state:
        type: "string"
        enum:
          - "deployed"
          - "pending"
          - "failed"
          - "deleted"
  ServiceInstance:

  Provisioner:
    type: object
    properties:
      id:
        type: "string"
        format: "uuid"
      name:
        type: "string"
      metadata:
        type: "object"

paths:
  /clusters:
    get:
      summary: List all clusters
      produces:
        - "application/json"
      responses:
        200:
          description: "Successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Cluster"

  /clusters/{id}:
    get:
      summary: Get information about cluster
      produces:
        - "application/json"
      parameters:
        - name: "id"
          in: "path"
          required: true
          type: string
      responses:
        200:
          description: "Successful operation"
          schema:
            $ref: "#/definitions/Cluster"
        400:
          description: "Invalid id supplied"
        404:
          description: "Cluster not found"
    delete:
      summary: "Delete cluster"
      produces:
        - "application/json"
      parameters:
        - name: "id"
          in: "path"
          required: true
          type: string
      responses:
        200:
          description: "Successful operation"
        400:
          description: "Invalid id supplied"
        404:
          description: "Cluster not found"

  /clusters/{id}/nodes:
    get:
      summary: Get information about cluster nodes
      parameters:
        - name: "id"
          in: "path"
          required: true
          type: string
      produces:
        - "application/json"
      responses:
        200:
          description: "Successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/ClusterNode"
        400:
          description: "Invalid id supplied"
        404:
          description: "Cluster not found"

  /clusters/{id}/services:
    get:
      summary: Get information about cluster services
      produces:
        - "application/json"
      parameters:
        - name: "id"
          in: "path"
          required: true
          type: string
      responses:
        200:
          description: "Successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/ClusterService"
        400:
          description: "Invalid id supplied"
        404:
          description: "Cluster not found"
          
  # provisioners
  /provisioners:
    get:
      summary: List all provisioners
      produces:
        - "application/json"
      responses:
        200:
          description: "Successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Provisioner"

  /provisioners/{id}:
    get:
      summary: Get information about provisioner
      produces:
        - "application/json"
      parameters:
        - name: "id"
          in: "path"
          required: true
          type: string
      responses:
        200:
          description: "Successful operation"
          schema:
            $ref: "#/definitions/Provisioner"
        400:
          description: "Invalid id supplied"
        404:
          description: "Cluster not found"
    delete:
      summary: "Delete provisioner"
      produces:
        - "application/json"
      parameters:
        - name: "id"
          in: "path"
          required: true
          type: string
      responses:
        200:
          description: "Successful operation"
        400:
          description: "Invalid id supplied"
        404:
          description: "Cluster not found"
      
