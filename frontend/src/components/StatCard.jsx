import { Card, CardContent, Typography } from "@mui/material";

export default function StatCard({ title, value }) {
  return (
    <Card
      sx={{
        width: "100%",
        maxWidth: 260,
        background: "#10213b",
        color: "white",
        borderRadius: 3,
        boxShadow: 5,
        textAlign: "center",
        p: 2,
      }}
    >
      <CardContent>
        <Typography
          variant="subtitle1"
          sx={{
            color: "#90caf9",
            fontWeight: "bold",
            mb: 1,
          }}
        >
          {title}
        </Typography>

        <Typography
          variant="h5"
          sx={{
            fontWeight: "bold",
            color: "#ffffff",
            wordBreak: "break-word",
          }}
        >
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
}