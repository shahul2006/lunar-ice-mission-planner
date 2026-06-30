import { useState } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import UploadCard from "../components/UploadCard";
import AnalyzeButton from "../components/AnalyzeButton";
import StatCard from "../components/StatCard";

import {
  uploadDataset,
  analyzeMission,
} from "../services/api";

export default function Home() {

  const navigate = useNavigate();

  const [ohrcFile, setOhrcFile] = useState(null);
  const [ohrcXmlFile, setOhrcXmlFile] = useState(null);
  const [tmcFile, setTmcFile] = useState(null);
  const [sarFile, setSarFile] = useState(null);

  // Stores the mission result
  const [missionResult, setMissionResult] = useState(null);

  const handleAnalyze = async () => {

    if (
      !ohrcFile ||
      !ohrcXmlFile ||
      !tmcFile ||
      !sarFile
    ) {
      alert("Please upload all required datasets.");
      return;
    }

    try {

      await uploadDataset(
        ohrcFile,
        ohrcXmlFile,
        tmcFile,
        sarFile
      );

      const result = await analyzeMission();

      // Show values on Home page
      setMissionResult(result);

      // Go to Dashboard after 2 seconds
      setTimeout(() => {

        navigate("/dashboard", {
          state: {
            result,
          },
        });

      }, 2000);

    } catch (error) {

      console.error(error);

      alert("Mission analysis failed.");

    }

  };

  return (
    <>
      <Navbar />

      <div
        style={{
          background: "#07111f",
          minHeight: "100vh",
          color: "white",
          padding: "40px",
        }}
      >
        <h1
          style={{
            textAlign: "center",
            marginBottom: "10px",
          }}
        >
          Lunar Mission Planner
        </h1>

        <p
          style={{
            textAlign: "center",
            color: "#b8c1cc",
            marginBottom: "50px",
          }}
        >
          Detection and Characterization of Subsurface Ice using
          Chandrayaan-2 OHRC, TMC-2 and DFSAR Data
        </p>

        <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: "30px",
            flexWrap: "wrap",
          }}
        >
          <UploadCard
            title="OHRC Dataset"
            selectedFile={ohrcFile}
            selectedXmlFile={ohrcXmlFile}
            onFileSelect={setOhrcFile}
            onXmlSelect={setOhrcXmlFile}
          />

          <UploadCard
            title="TMC-2 Dataset"
            selectedFile={tmcFile}
            onFileSelect={setTmcFile}
          />

          <UploadCard
            title="DFSAR Dataset"
            selectedFile={sarFile}
            onFileSelect={setSarFile}
          />
        </div>

        <AnalyzeButton onAnalyze={handleAnalyze} />

        <h2
          style={{
            textAlign: "center",
            marginTop: "60px",
            marginBottom: "30px",
          }}
        >
          Mission Statistics
        </h2>
                <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: "20px",
            flexWrap: "wrap",
            marginBottom: "60px",
          }}
        >
          <StatCard
            title="Ice Volume"
            value={
              missionResult
                ? `${missionResult.ice_volume.toFixed(2)} m³`
                : "--"
            }
          />

          <StatCard
            title="Landing Site"
            value={
              missionResult
                ? `(${missionResult.landing_site[0]}, ${missionResult.landing_site[1]})`
                : "--"
            }
          />

          <StatCard
            title="Mission Score"
            value={
              missionResult
                ? missionResult.mission_score.toFixed(2)
                : "--"
            }
          />

          <StatCard
            title="Hazard Zones"
            value={
              missionResult
                ? missionResult.hazard_zones
                : "--"
            }
          />

          <StatCard
            title="Detected Craters"
            value={
              missionResult
                ? missionResult.crater_count
                : "--"
            }
          />

          <StatCard
            title="Path Length"
            value={
              missionResult
                ? missionResult.path_length
                : "--"
            }
          />
        </div>

        <Footer />

      </div>
    </>
  );
}