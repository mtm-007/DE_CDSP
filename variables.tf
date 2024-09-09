variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my_tera_cred.json"
}

variable "project" {
  description = "Project"
  default     = "resonant-time-434823-n0"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "MY BigQuery dataset name"
  default     = "de_zm_dataset"
}

variable "gcp_bucket_name" {
  description = "MY Bucket storage name"
  default     = "resonant-time-434823-n0-de-zm-terra-bucket"
}

variable "gcp_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"

}