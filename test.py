import json

# c = """{[{
#     "a":"b"
# }]}"""
# print c
# print json.loads(c)
d = list()
with open("test.json", "r") as f:
    b = json.load(f)
for c in b["rows"]:
    d.append({"match": {"av":c["SEARCH_KWRD"]}})
print json.dumps(d)

exit()



kwrd = """7ev3n

8.t

9002

AbaddonPOS

abantes

Abbath

ACBackdoor

ACEHASH

AcridRain

Acronym

AdamLocker

AdKoob

AdultSwine

AdvisorsBot

AdWind

Adylkuzz

Tesla

Agent.BTZ

AhMyth

AIRBREAK

AirDropBot

Aldibot

Alina

Allaple

Alma

AlmaLocker

ALPC

Alphabet

AlphaLocker

AlphaNC

Alreay

Alureon

Amadey

AMTsol

Anatova

Andromeda

AndroMut

AndroRAT

Anel

Ani-Shell

ANTAK

AnteFrigus

Antilam

Anubis

AnubisSpy

apk.lazarus_elf

Apocalipto

Apocalypse

AppleJeus

APT3

ArdaMax

Arefty

Arik

Arkei

ARS

Artra

Asacub

AscentLoader

Ashas

ASPC

Asprox

Asruex

Astaroth

AsyncRAT

AthenaGo

ATI-Agent

ATMii

ATMitch

Atmosphere

ATMSpitter

Attor

August

Auriga

Aurora

AutoCAD

AvastDisabler

AVCrypt

Maria

Aveo

Avzhan

Ayegent

azazel

Azorult

Babar

BabyLon

BABYMETAL

BabyShark

BACKBEND

BackNet

backspace

BackSwap

BADCALL

BadEncript

badflick

BadNews

Bagle

Bahamut

Baldr

BalkanDoor

BalkanRAT

Bamital

Banatrix

bangat

Banjori

Bankshot

Banload

Bart

Bashlite

BatchWiper

Batel

Bateleur

BBSRAT

BCMPUPnP_Hunter

Beapy

Bedep

beendoor

Bella

BELLHOP

Belonard

Berbomthum

BernhardPOS

BetaBot

Bezigate

BfBot

BianLian

BillGates

BioData

Biscuit

Bitsran

Bitter

BI_D

BKA

BLACKCOFFEE

BlackEnergy

BlackPOS

BlackRemote

BlackRevolution

BlackRouter

Blackruby

BlackShades

Blackworm

BLINDTOAD

Boaxxe

Bohmini

Bolek

BONDUPDATER

BOOSTWRITE

BOOTWRECK

Bouncer

Bozok

BRAIN

Brambul

BRATA

BravoNC

BreachRAT

Breakthrough

Bredolab

BrickerBot

BrushaLoader

BrutPOS

BS2005

BTCWare

BUBBLEWRAP

Buhtrap

Bundestrojaner

Bunitu

BusyGasper

Buterat

Buzus

BYEBY

c0d0so0

CabArt

CACTUSTORCH

CadelSpy

CamuBot

Cannibal

Cannon

Carbanak

Carberp

Cardinal

Careto

CarrotBat

Casper

Catchamas

Catelites

CCleaner

CDorked

CenterPOS

Cerber

Cerberus

Cerbu

Chainshot

Chamois

Chaperone

Chapro

Charger

ChChes

CHEESETRAY

CherryPicker

ChewBacca

CHINACHOPPER

Chinad

Chir

Chrysaor

Chthonic

Citadel

CLASSFON

CLEANTOAD

Maximus

Clientor

ClipBanker

Clipper

Duke

CMSBrute

CMSTAR

CoalaBot

Cobalt

Cobian

CobInt

Cobra

CockBlocker

CodeKey

Cohhoc

Coinminer

CoinThief

Coldroot

Colony

Combojack

Combos

CometBot

ComodoSec

COMpfun

Computrace

ComradeCircle

concealment_troy

Conficker

Confucius

Connic

Contopee

CookieBag

Corebot

CoreDN

Coreshell

Corona

Cotx

CpuMeaner

Cpuminer

Cr1ptT0r

crackshot

CradleCore

CREAMSICLE

CreativeUpdater

Credraptor

Crenufs

Crimson

Crisis

CrossRAT

Crossrider

CROSSWALK

Cryakl

CryLocker

CrypMic

Crypt0l0cker

CryptoFortress

CryptoLocker

CryptoLuck

CryptoMix

CryptoNight

CryptoRansomeware

Cryptorium

CryptoShield

CryptoShuffler

Cryptowall

CryptoWire

CryptXXXX

CsExt

Cuegoe

Cueisfry

CukieGrab

Cutlet

Cutwail

CyberGate

CyberSplitter

CycBot

DADJOKE

Dairy

DanaBot

danbot

DarkComet

DarkHotel

DarkMegi

Darkmoon

DarkPulsar

DarkRat

DarkShell

Darksky

DarkStRat

DarkTequila

Darktrack

DarthMiner

Daserf

Datper

DDKONG

DeathRansom

Decebal

Delta(Alfa,Bravo,

Dented

DeputyDog

DeriaLock

Derusbi

Devil's

Dexter

Dharma

DiamondFox

DILLJUICE

Dimnie

DirCrypt

DispenserXFS

DistTrack

Divergent

DMA

DMSniff

DNSChanger

DNSMessenger

DNSpionage

DNSRat

Dockster

DogHousePower

Dok

DoppelPaymer

Dorshel

DoubleLocker

DoublePulsar

Downdelph

Downeks

DownPaper

Downrage

DramNudge

DreamBot

Dridex

DRIFTPIN

Dripion

DROPSHOT

Dtrack

DualToy

DUBrute

Dumador

Dummy

DuQu

Duuzer

Dvmap

DYEPACK

Dyre

EASYNIGHT

Ebury

Echobot

EDA2

EHDevel

Eleanor

ELECTRICFISH

ElectricPowder

elf.vpnfilter

elf.wellmess

Elirks

Elise

ELMER

Emdivi

Emotet

Empire

Enfal

EquationDrug

Equationgroup

Erebus

Eredel

Eris

EternalPetya

EtumBot

Evilbunny

EvilGnome

EvilGrab

EVILNUM

EvilOSX

EvilPony

Evrial

Exaramel

Excalibur

Exile

ExoBot

Exodus

ext4

Pyramid

FailyTale

Pornhub

FakeDGA

FakeGram

FakeRean

FakeSpy

FakeTC

Fanny

FantomCrypt

Farseer

FastCash

FastPOS

FBot

FEimea

Felismus

Felixroot

Feodo

FileCoder

FileIce

Final1stSpy

FindPOS

FinFisher

Fireball

FireCrypt

FireMalv

FirstRansom

Flame

FlashBack

FLASHFLOOD

FlawedAmmyy

FlawedGrace

FlexiSpy

FlexNet

FlokiBot

floodor

FlowerShop

Floxif

Flusihoc

FlyingDutchman

Fobber

forbiks

Formbook

FormerFirstRAT

FortuneCrypt

Freenki

FriedEx

FruitFly

FTCODE

FunkyBot

Furtim

FuxSocy

GalaxyLoader

gamapos

Gameover

Gamotrol

Gandcrab

Gaudox

Gauss

Gazer

gcman

GearInformer

GEARSHIFT

GEMCUTTER

Get2

GetMail

GetMyPass

Gh0stnet

Ghole

Ghost

GhostAdmin

GhostCtrl

GhostMiner

Ginp

GlanceLove

Glasses

GlassRAT

GlitchPOS

Globe

GlobeImposter

GlooxMail

Glupteba

GoBotKR

Godlua

Godzilla

Goggles

GoldDragon

GoldenEye

GoldenRAT

Golroted

Goodor

GoogleDrive

GooPic

GootKit

GovRAT

Gozi

GPCode

GPlayed

GrabBot

Graftor

GrandSteal

Grateful

Gratem

Gravity

GREASE

GreedyAntd

GreenShaitan

GreyEnergy

Griffon

GRILLMARK

GROK

gsecdump

GuiInject

GUP

Gustuff

H1N1

Hacksfase

HackSpy

Haiduc

Hajime

Hakai

Hakbit

HALFBAKED

Hamweq

Hancitor

HandyMannyPot

HappyLocker

HARDRAIN

Harnig

Havex

HAWKBALL

HawkEye

HDMR

Helauto

Helminth

Heloag

HenBox

Herbst

Heriplor

Hermes

HeroRAT

HerpesBot

HesperBot

Hi-Zor

Hidden

HiddenAd

HiddenLotus

HiddenTear

HiddenWasp

Hide

HideDRV

HIGHNOON

HIGHNOON.BIN

HIGHNOTE

HiKit

himan

HLUX

homefry

HOPLIGHT

HOTWAX

Houdini

HtBot

HTML5

htpRAT

HTran

HttpBrowser

httpdropper

http_troy

Hussar

Hworm

Hydra

HyperBro

Ice

IcedID

Icefog

IDKEY

IISniff

Iloveyou

Imecab

Imminent

iMuler

Industroyer

Infy

InnaputRAT

inter

InvisiMole

Reaper

Irc16

IRONHALO

IRRat

ISFB

ISMAgent

ISMDoor

iSpy

ISR

IsraBye

IsSpace

JackPOS

JadeRAT

Jaff

Jager

Jaku

jason

JasperLoader

Jasus

JavaDispCash

JCry

JenX

Jigsaw

Jimmy

Joanap

Joao

Joker

Jolob

JQJSNICKER

jRAT

JripBot

jSpy

JUMPALL

KAgent

Kaiten

Karagany

Kardon

Karius

Karkoff

KasperAgent

Kazuar

Kegotip

Kelihos

KeRanger

kerberods

KerrDown

Ketrican

KevDroid

KeyBase

KeyBoy

Keydnap

KEYMARBLE

KHRAT

Kikothac

KillDisk

Kimsuky

KINS

Kitmos

KleptoParasite

KLRD

Koadic

KokoKrypt

Koler

Komplex

KOMPROGO

Konni

KoobFace

KopiLuwak

Korlia

Kovter

KPOT

Kraken

KrBanker

KrDownloader

Kronos

KSL0T

Kuaibu

Kuluoz

Kurton

Kutaki

Kwampirs

L0rdix

Lady

Lambert

Lamdelin

Laoshu

LatentBot

Laturo

Laziok

LazyCat

Leash

Leouncia

Lethic

Leverage

Liderc

LightNeuron

Ligsterac

Lilith

LiLock

lilyofthevalley

limedownloader

limeminer

LimeRAT

Limitail

Listrix

LiteHTTP

LockerGoga

LockPOS

Locky

Loda

Logedrut

LogPOS

LoJax

Loki

LokiBot

LONGWATCH

looChiper

Lookback

LOWBALL

LOWKEY

LuckyCat

Luminosity

LunchMoney

Lurk

Luzo

Lyposit

MacDownloader

Machete

MacInstaller

MacRansom

MacSpy

MacVX

MadMax

Magala

magecart

Magniber

Maintools.js

MajikPos

Makadocs

MakLoader

Maktub

MalumPOS

Mamba

MaMi

ManameCrypt

Mangzamel

Manifestus

ManItsMe

Maoloa

MAPIget

Marap

Marcher

Mariposa

Masuta

Matrix

Matryoshka

Matsnu

MazarBot

Maze

MBRlock

Mebromi

MECHANICAL

Medre

Medusa

MegaCortex

MeguminTrojan

Merlin

MESSAGETAP

Metamorfo

Mewsei

Miancha

Micrass

Microcin

Micropsia

MiKey

Mikoponi

MILKMAID

MimiKatz

MiniASP

MiniDuke

Mirage

MirageFox

Mirai

Misdat

Misfox

Miuref

MM

MobiRAT

Mocton

ModPOS

Moker

Mokes

Mole

Molerat

Monero

Monokle

MoonWind

Moose

More_eggs

Morphine

Morto

Mosquito

Moure

mozart

MPKBot

MrBlack

MS

Mudwater

Mughthesec

Multigrain

murkytop

Murofet

Mutabaha

MyDoom

MyKings

MyloBot

MysteryBot

N40

Nabucur

NACHOCHEESE

Nagini

Naikon

NanHaiShu

Nanocore

NanoLocker

Narilam

Nautilus

NavRAT

Necurs

Nemim

Nemty

neshta

NESTEGG

NetC

NETEAGLE

NetKey

Netrepser

NetSupportManager

NetTraveler

NetWire

Neuron

Neutrino

NewCore

NewCT

NewPosThings

NewsReels

Nexster

Nextcry

NexusLogger

Ngioweb

NgrBot

Nightmare

nitlove

Nitol

NjRAT

Nocturnal

Nokki

Nozelesn

nRansom

NVISOSPIT

Nymaim

Nymaim2

OceanLotus

Oceansalt

Octopus

OddJob

Odinaff

OilRig

Okrum

OLDBAIT

Olympic

Olyx

OmniRAT

OneKeyLocker

ONHAT

Oni

OnionDuke

OnlinerSpambot

OopsIE

Opachki

OpBlockBuster

OpGhoul

ORANGEADE

OrcaRAT

Orcus

Ordinypt

ostap

Outlook

Overlay

OvidiyStealer

owaauth

Owari

Ozone

PadCrypt

paladin

PandaBanker

parasite_http

PAS

Patcher

Surveillance

Peepy

Penco

Penquin

PerlBot

Persirai

PetrWrap

Petya

pgift

PhanDoor

Philadephia

Phobos

PHOREAL

Phorpiex

PICKPOCKET

PintSized

pipcreat

pirpi

Pirrit

Pitou

PittyTiger

Pkybot

PLAINTEE

playwork

PLEAD

Ploutus

ployx

PlugX

Plurox

pngdowner

PocoDown

Podec

PoisonIvy

PoisonCarp

poisonplug

Poldat

Polyglot

Pony

PoohMilk

PoorWeb

Popcorn

portless

poscardstealer

PoshC2

POSHSPY

PoSlurp

Poweliks

PowerBrace

PowerCat

PowerDuke

powerkatz

POWERPIPE

PowerPool

PowerRatankba

PowerShellRunner

powershell_web_backdoor

PowerShower

Powersniff

POWERSOURCE

PowerSpritz

POWERSTATS

POWERTON

PowerWare

Powmet

POWRUNER

prb_backdoor

Predator

Premier

PresFox

Prikormka

Prilex

PrincessLocker

Project

proteus

Proton

ProtonBot

PsiX

PSLogger

Pteranodon

PubNubRAT

Punkey

pupy

PureLocker

Pushdo

Putabmow

PvzOut

Pwnet

pwnpos

Pykspa

PyLocky

Qaccel

Qadars

QakBot

Qarallax

Qealler

QHost

QNAPCrypt

QRat

QSnatch

QtBot

QUADAGENT

QuantLoader

Quasar

QUICKCAFE

Qulab

r2r2

r980

Raccoon

Radamant

RadRAT

Rakhni

Rakos

Rambo

Ramdo

Ramnit

Ranbyus

Ranscam

Ransoc

Ransomlock

Rapid

RapidStealer

Rarog

rarstar

RaspberryPiBotnet

Ratabanka

RatabankaPOS

RatSnif

Ratty

rat_hodin

RawPOS

Raxir

rbs_srv

RCS

rdasrv

ReactorBot

Reaver

Red

RedAlert2

RedAlpha

RedLeaves

RedPepper

RedSalt

REDSHAWL

Redyms

reGeorg

Regin

Remcos

Remexi

Remsec

Remy

reptile

Rerdom

Retadup

Retefe

Revenge

Rex

RGDoor

Rietspoof

Rifdoor

Rikamanu

Riltok

Rincux

Ripper

Rising

RMS

Mantis

RobinHood

Roboto

rock

Rockloader

Rofin

RogueRobin

RogueRobinNET

Rokku

RokRAT

Rombertik

Romeo(Alfa,Bravo,

Roopirs

Rootnik

Roseam

RotorCrypt

Rover

Rovnix

Royal

RoyalCli

Rozena

RTM

rtpos

Ruckguv

Rumish

running_rat

Rurktar

Rustock

Ryuk

Saefko

SAGE

Sakula

Salgorea

Sality

SamSam

Sanny

Saphyra

SappyCache

Sarhust

Sasfis

Satan

Satana

Sathurbot

Satori

Sauron

scanbox

ScanPOS

Scarabey

Schneiken

Scote

Scranos

ScreenLocker

SDBbot

SeaDaddy

SeaSalt

SectopRAT

SeDll

Sedreco

Seduploader

SendSafe

Serpico

ServHelper

shadowhammer

ShadowPad

Shakti

SHAPESHIFT

shareip

SHARPKNOT

SHARPSTATS

ShellBind

ShellLocker

Shifu

Shim

SHIPSHAPE

Shishiga

Shujin

Shurl0ckr

Shylock

SideWinder

Sierra(Alfa,Bravo,

Siggen6

Silence

Silex

Silon

Siluhdur

Simda

Sinowal

Sisfader

Skarab

Skimer

Skipper

Skygofree

Skyplex

skyrat

Slave

Slempo

Slingshot

Sliver

sLoad

Slocker

SLUB

smac

SmokeLoader

Smominru

Smrss32

SmsAgent

SMSspy

Snatch

SnatchLoader

SNEEPY

Snifula

Snojan

SNS

Sobaken

Sobig

Socks5

SocksBot

Sodinokibi

Solarbot

soraya

Sorgu

SOUNDBITE

SPACESHIP

Spamtorte

Sparkle

SpeakUp

Spedear

Spora

SpyBanker

SpyBot

SpyEye

SpyNote

SQLRat

SquirtDanger

SSHDoor

SslMM

Stabuniq

Stampedo

Stantinko

StarCruft

StarLoader

StarsyPound

StartPage

Mango

StealthAgent

StealthWorker

StegoLoader

Stinger

STOP

Stration

Stresspaint

StrongPity

Stuxnet

Sunless

SunOrcal

SuppoBox

SupremeBot

sustes

Svpeng

swen

Switcher

Sword

sykipot

SynAck

SyncCrypt

SynFlooder

Synth

Sys10

Syscon

SysGet

SysKit

Sysraw

SysScan

SystemBC

systemd

Szribi

TabMsgSQL

taidoor

TalentRAT

Taleret

Tandfuy

Tapaoux

Tarsip

Tater

tDiscoverer

TDTESS

TeamBot

TefoSteal

TeleBot

TeleDoor

TeleRAT

Tempedreve

TemptingCedar

Terminator

Termite

TeslaCrypt

TFlower

Thanatos

ThreeByte

ThumbThief

ThunderShell

Thunker

Tidepool

Tinba

TinyLoader

TinyMet

TinyNuke

TinyTyphon

TinyZ

TinyZbot

Tiop

Titan

Tofsee

TONEDEAF

Torii

TorrentLocker

tRat

TreasureHunter

Triada

TrickBot

Triout

Triton

Trochilus

Troldesh

Trump

tsh

Tsifiri

Tsunami

Turla

TURNEDUP

TwoFace

Tyupkin

UACMe

UDPoS

UFR

Uiwix

Umbreon

Unlock92

UPAS

Upatre

Urausy

UrlZone

Uroburos

VALUEVAULT

vamp

vanillarat

Varenyky

Vawtrak

VegaLocker

Velso

Venus

Vermin

Vflooder

vidar

Viper

virdetdoor

Virut

VM

Vobfus

Volgmer

Vreikstadi

vSkimmer

w32times

WallyShack

WannaCryptor

WaterMiner

WaterSpout

WebC2-AdSpace

WebC2-Ausov

WebC2-Bolid

WebC2-Cson

WebC2-DIV

WebC2-GreenCat

WebC2-Head

WebC2-Kt3

WebC2-Qbp

WebC2-Rave

WebC2-Table

WebC2-UGX

WebC2-Yahoo

WebMonitor

WellMess

WildFire

win.innfirat

win.purplefox

win.redaman

win.spynet_rat

win.unidentified_005

win.xpertrat

WindTail

winlog

WinMM

Winnti

WinPot

Winsloader

Wipbot

WireLurker

Wirenet

WireX

witchcoven

WMImplant

WndTest

Wonknu

woody

Woolger

WORMHOLE

WSCSPL

WSO

X-Agent

X-Tunnel

Xaynnalc

Xbash

Xbot

XBTL

XFSADM

XFSCashNCR

XLoader

XOR

Xpan

XPCTRA

XRat

XSLCmd

xsPlus

Xtreme

XTunnel

Xwo

xxmm

Yahoyah

Yatron

yayih

YellYouth

Yoddos

Yort

YoungLotus

yty

Zebrocy

Zedhou

Zen

ZeroAccess

ZeroEvil

ZeroLocker

ZeroT

Zeus

ZeusAction

Zezin

ZhCat

ZhMimikatz

Zloader

Zollard

ZooPark

ZoxPNG

Ztorg

ZUpdater

ZXShell

Zyklon"""

kwrd_list = kwrd.split("\n\n")
print json.dumps(kwrd_list)