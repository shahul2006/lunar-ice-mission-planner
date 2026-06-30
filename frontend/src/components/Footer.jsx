import { Box, Typography } from "@mui/material";

export default function Footer() {
  return (
    <Box
      sx={{
        marginTop: "60px",
        padding: "20px",
        textAlign: "center",
        background: "#081229",
        color: "#b8c1cc",
        borderTop: "1px solid #1f2d4d",
      }}
    >
      <Typography variant="body2">
        © 2026 Chandrayaan-2 Mission Planner
      </Typography>

      <Typography variant="body2" sx={{ mt: 1 }}>
        Developed for ISRO Bharatiya Antariksh Hackathon
      </Typography>
    </Box>
  );
}