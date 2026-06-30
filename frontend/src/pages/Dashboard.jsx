import { useLocation, Navigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import ImageCard from "../components/ImageCard";
import StatCard from "../components/StatCard";

const BASE_URL = "http://127.0.0.1:8000/outputs";

export default function Dashboard() {

  const location = useLocation();

  const result = location.state?.result;

  if (!result) {
    return <Navigate to="/" replace />;
  }

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
            marginBottom: "15px",
          }}
        >
          Mission Dashboard
        </h1>

        <p
          style={{
            textAlign: "center",
            color: "#90caf9",
            marginBottom: "40px",
          }}
        >
          Chandrayaan-2 Lunar South Pole Analysis
        </p>

        {/* ================= Statistics ================= */}

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3, 1fr)",
            gap: "25px",
            maxWidth: "950px",
            margin: "0 auto 60px auto",
            justifyItems: "center",
          }}
        >
          <StatCard
            title="Ice Volume"
            value={`${result.ice_volume.toFixed(2)} m³`}
          />

          <StatCard
            title="Landing Site"
            value={`(${result.landing_site[0]}, ${result.landing_site[1]})`}
          />

          <StatCard
            title="Mission Score"
            value={result.mission_score.toFixed(2)}
          />

          <StatCard
            title="Hazard Zones"
            value={result.hazard_zones}
          />

          <StatCard
            title="Detected Craters"
            value={result.crater_count}
          />

          <StatCard
            title="Path Length"
            value={result.path_length}
          />
        </div>

        {/* ================= Images ================= */}

        <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: "30px",
            flexWrap: "wrap",
            marginBottom: "60px",
          }}>
        <ImageCard
            title="OHRC Image"
            image={`${BASE_URL}/ohrc.png`}
          />

          <ImageCard
            title="Ice Probability"
            image={`${BASE_URL}/ice_probability.png`}
          />

          <ImageCard
            title="Hazard Map"
            image={`${BASE_URL}/hazard_map.png`}
          />

          <ImageCard
            title="Rover Traverse"
            image={`${BASE_URL}/rover_path.png`}
          />
        </div>

        <Footer />
      </div>
    </>
  );
}