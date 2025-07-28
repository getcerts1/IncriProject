variable "location" {
  default = "westus"
  type = string

}

variable "acr_name" {
  default = "incriprojectacr"
  type = string
}

variable "aks_name" {
  default = "incricluster001"
  type = string
}

variable "node_count" {
  default = 3
  type = number
}