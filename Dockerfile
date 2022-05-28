#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build
WORKDIR /src
COPY ["SnappFood.csproj", "."]
RUN dotnet restore "./SnappFood.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "SnappFood.csproj" -c Release -o /app/build

RUN dotnet test "SnappFood.csproj" --logger "trx;LogFileName=SnappFood.trx" 

FROM build AS publish
RUN dotnet publish "SnappFood.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "test", "SnappFood.dll"]

