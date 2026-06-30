import { Button } from "@mui/material";
import RocketLaunchIcon from "@mui/icons-material/RocketLaunch";

export default function AnalyzeButton({ onAnalyze }) {
  return (
    <div
      style={{
        marginTop: "50px",
        display: "flex",
        justifyContent: "center",
      }}
    >
      <Button
        variant="contained"
        size="large"
        startIcon={<RocketLaunchIcon />}
        onClick={onAnalyze}
        sx={{
          background: "#00c853",
          color: "white",
          px: 6,
          py: 1.5,
          fontSize: "18px",
          borderRadius: "30px",
          "&:hover": {
            background: "#00b248",
          },
        }}
      >
        Analyze Mission
      </Button>
    </div>
  );
}