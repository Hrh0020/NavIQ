import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Sidebar } from "@/components/ui/sidebar";
import { LayoutDashboard, BarChart2, Settings } from "lucide-react";

export default function NavIQ() {
  return (
    <div className="flex min-h-screen bg-gray-100 font-sans">
      <Sidebar className="w-20 lg:w-64 bg-[#0A2342] text-white p-4 shadow-lg">
        <div className="flex flex-col space-y-4 mt-10">
          <div className="flex items-center space-x-2">
            <LayoutDashboard size={20} />
            <span className="hidden lg:inline">Dashboard</span>
          </div>
          <div className="flex items-center space-x-2">
            <BarChart2 size={20} />
            <span className="hidden lg:inline">Analytics</span>
          </div>
          <div className="flex items-center space-x-2">
            <Settings size={20} />
            <span className="hidden lg:inline">Settings</span>
          </div>
        </div>
      </Sidebar>

      <main className="flex-1 p-6 space-y-6">
        <h1 className="text-3xl font-bold text-[#0A2342]">NavIQ Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <Card className="rounded-2xl shadow p-4">
            <CardContent>
              <h2 className="text-xl font-semibold text-[#1E3A8A]">Net Asset Value</h2>
              <p className="text-2xl mt-2">$248,400</p>
            </CardContent>
          </Card>

          <Card className="rounded-2xl shadow p-4">
            <CardContent>
              <h2 className="text-xl font-semibold text-[#1E3A8A]">Premium Earned</h2>
              <p className="text-2xl mt-2">$6,740</p>
            </CardContent>
          </Card>

          <Card className="rounded-2xl shadow p-4">
            <CardContent>
              <h2 className="text-xl font-semibold text-[#1E3A8A]">Capital Deployment</h2>
              <p className="text-2xl mt-2">82%</p>
            </CardContent>
          </Card>
        </div>

        <Button className="bg-[#00BFFF] text-white hover:bg-[#009ACD] rounded-xl mt-6">
          Update Portfolio Data
        </Button>
      </main>
    </div>
  );
}
