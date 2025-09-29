import Link from "next/link";
import Image from "next/image";
import { House } from "lucide-react";
export default function HomeButton() {
  return (
    <Link href="/">
      <House/>
    </Link>
  );
}
