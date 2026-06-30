import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 300000,
});

// -------------------------------------
// Upload OHRC IMG, OHRC XML, TMC and SAR
// -------------------------------------

export const uploadDataset = async (
  ohrcFile,
  ohrcXmlFile,
  tmcFile,
  sarFile
) => {

  const formData = new FormData();

  formData.append("ohrc", ohrcFile);
  formData.append("ohrc_xml", ohrcXmlFile);
  formData.append("tmc", tmcFile);
  formData.append("sar", sarFile);

  const response = await api.post(
    "/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

// -------------------------------------
// Run Mission Analysis
// -------------------------------------

export const analyzeMission = async () => {

  const response = await api.post("/analyze");

  return response.data;
};

// -------------------------------------
// Health Check
// -------------------------------------

export const checkServer = async () => {

  const response = await api.get("/health");

  return response.data;
};

export default api;